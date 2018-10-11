import React from 'react';
import {
  Container,
  Row,
  Col,
  Pagination,
  PaginationItem,
  PaginationLink,
  Progress,
} from 'reactstrap';

import ImageCard from './ImageCard'
import FilterList from './FilterList'
import Error from './Error'
import ImageModal from './ImageModal'

export default class ImageGrid extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      loaded: false,
      tags: null,
      ids: [],
      matches: [],
      filters: {},
      start: 0,
      end: 12,
      modalOpen: false,
    }

    this.nextPage = this.nextPage.bind(this)
    this.prevPage = this.prevPage.bind(this)
    this.choosePage = this.choosePage.bind(this)
    this.filter = this.filter.bind(this)
    this.callback = this.callback.bind(this)
    this.updateTags = this.updateTags.bind(this)
    this.toggle = this.toggle.bind(this)
    this.setModal = this.setModal.bind(this)
    this.markerFilter = this.markerFilter.bind(this)

    this.image_tags = {}
    this.tag_dict = {}
    this.tag_idx = {}
    this.raw_tags = {}
    this.initialized = false
    this.defs = require('../assets/pancreatlas/definitions.json')
  }

  componentDidMount() {
    fetch(`${process.env.REACT_APP_API_URL}/tagsets/`)
      .then(res => res.json())
      .then(
        (tresult) => {
          this.raw_tags = tresult
          for (let o of Object.keys(tresult)) {
            if ('set_name' in tresult[o]) {
              this.tag_idx[tresult[o].set_name] = o
              this.tag_dict[tresult[o].set_name] = []
              let extras = ['depth 1', 'depth 2', 'depth 3']
              for (let t of Object.keys(tresult[o].tags)) {
                if (extras.indexOf(t) === -1) {
                  this.tag_dict[tresult[o].set_name].push(t)
                } else {
                  delete this.raw_tags[o].tags[t]
                }
              }
            }
          }
          fetch(`${process.env.REACT_APP_API_URL}/datasets/${this.props.did}/get-images`)
            .then(res => res.json())
            .then(
              (result) => {
                this.setState({
                  loaded: true,
                  ids: result,
                  matches: Object.keys(result),
                  page: 0
                });
                this.updateTags(true)
                // this.filter(this.props.filters)
              })
            .catch(err => {
              console.log(err)
              this.setState({
                loaded: false,
                error: err
              })
            });
        }
      )
  }

  componentDidUpdate(prevProps, prevState) {
    if (JSON.stringify(prevState.filters) !== JSON.stringify(this.state.filters)) {
      this.updateTags(false)
    }
  }

  updateTags(shouldDelete) {
    let app_tags = JSON.parse(JSON.stringify(this.raw_tags));
    for (let key of this.state.matches) {
      for (let tag of Object.keys(this.tag_dict)) {
        let intersection = this.state.ids[key].filter(val => -1 !== this.tag_dict[tag].indexOf(val))
        if (intersection.length > 0) {
          for (let tval of intersection) {
            app_tags[this.tag_idx[tag]].tags[tval]++
          }
        }
      }
    }
    if (shouldDelete) {
      for (let tagset of Object.keys(app_tags)) {
        for (let tag of Object.keys(app_tags[tagset].tags)) {
          if (app_tags[tagset].tags[tag] === 0) {
            delete app_tags[tagset].tags[tag]
            delete this.raw_tags[tagset].tags[tag]
          }
        }
      }
    }
    this.setState({
      tags: app_tags
    })
  }

  choosePage(new_page) {
    this.setState({
      page: new_page
    })
  }

  nextPage() {
    if (this.state.page >= Math.ceil(this.state.images.length / 12)) { return false; }
    let new_page = this.state.page + 1
    this.setState({
      page: new_page
    })
  }

  prevPage() {
    if (this.state.page <= 0) { return false; }
    let new_page = this.state.page - 1
    this.setState({
      page: new_page
    })
  }

  filter(tagList) {
    let empty = true
    for (let key of Object.keys(tagList)) {
      if (tagList[key].length > 0) {
        empty = false
        break
      }
    }

    if (empty) {
      this.setState({
        filters: {AGE: []},
        matches: Object.keys(this.state.ids)
      })
    } else {
      let tmp = JSON.parse(JSON.stringify(Object.keys(this.state.ids)))
      let allIds = JSON.parse(JSON.stringify(this.state.ids))
      for (let id of Object.keys(allIds)) {
        let match = true
        for (let keyset of Object.keys(tagList)) {
          if(keyset !== 'AGE' || (keyset === 'AGE' && tagList[keyset].length > 0)){
            let intersection = tagList[keyset].filter(tag => -1 !== allIds[id].indexOf(tag))
            if (intersection.length <= 0) {
              match = false
              break
            }  
          }
        }
        if (!match) {
          tmp.splice(tmp.indexOf(id), 1)
        }
      }
      this.setState({
        filters: tagList,
        matches: tmp
      })
    }
  }

  markerFilter(marker){
    let currentFilters = this.state.filters
    if(Object.keys(currentFilters).indexOf('MARKER') === -1){
      currentFilters['MARKER'] = []
    }
    if(currentFilters['MARKER'].indexOf(marker) === -1){
      currentFilters['MARKER'].push(marker)
    }
    this.filter(currentFilters)
  }

  callback(iid, tags) {
    this.image_tags[iid] = tags
  }

  toggle() {
    this.setState({
      modalOpen: !this.state.modalOpen
    })
  }

  setModal(imgInfo) {
    fetch(`${process.env.REACT_APP_API_URL}/images/${imgInfo}`)
      .then(res => res.json())
      .then(
        (result) => {
          let path = result.kvals['File path'].val
          let re = /([0-9]+-[0-9]+-[0-9]+)?(\/[^/]+\.[a-z]+)$/
          let age_re = /^(G?)(\d+)(.\d)?(d|w|mo|y)(\+\dd)?$/
          let matches = re.exec(path)
          result.kvals['File path'].val = matches[0]
          result.kvals['Donor info - Age'].val = result.tags.filter(val => age_re.test(val))[0]
          this.setState({
            modalData: {
              img_id: imgInfo,
              img_data: result.kvals,
              path_path: result.pathpath
            }
          })
          this.toggle()
        })
      .catch(err => {
        this.setState({
          loaded: false,
          error: err
        })
      });
  }

  render() {
    if (this.state.loaded) {
      let pages = []
      for (let i = 0; i < Math.ceil(this.state.matches.length / 16); i++) {
        if (i === this.state.page) {
          pages.push(<PaginationItem key={i} active><PaginationLink onClick={(e) => this.choosePage(i)}>{i + 1}</PaginationLink></PaginationItem>)

        } else {
          pages.push(<PaginationItem key={i}><PaginationLink onClick={(e) => this.choosePage(i)}>{i + 1}</PaginationLink></PaginationItem>)
        }
      }

      let img_grid = []
      let start = 16 * this.state.page
      let end = start + 16
      let slice = this.state.matches.slice(start, end);
      while (slice.length) {
        img_grid.push(slice.splice(0, 4));
      }


      // C:\Users\messmej\Documents\Projects\pancreatlas\react\src\assets\pancreatlas\thumbs\55.jpg

      return (
        <div className="image-grid">
          <h5 className='view-counter'>You are currently viewing {this.state.matches.length} out of a possible {Object.keys(this.state.ids).length} images</h5>
          <Container>
            <Row className="pancreatlas-row">
              <Col md="2">
                <FilterList ageGroup={this.props.groupName} tags={this.state.tags} filters={this.state.filters} callback={this.filter} />
              </Col>
              <Col md="10">
                {img_grid.map((item, idx) => (
                  <Row key={idx} className="image-row pancreatlas-row">
                    {item.map((image, idx) =>
                      <Col key={idx} md="3">
                        <ImageCard key={image} iid={image} callback={this.setModal} filterCallback={this.markerFilter} />
                      </Col>
                    )}
                  </Row>
                ))}
                <Row className="pancreatlas-row">
                  <Col md="12">
                    <Pagination>
                      <PaginationItem>
                        <PaginationLink previous href="#" onClick={this.prevPage} />
                      </PaginationItem>
                      {pages}
                      <PaginationItem>
                        <PaginationLink next href="#" onClick={this.nextPage} />
                      </PaginationItem>
                    </Pagination>
                  </Col>
                </Row>
              </Col>
            </Row>
            <ImageModal toggle={this.toggle} isOpen={this.state.modalOpen} modalData={this.state.modalData} />
          </Container>
        </div>
      );

    } else if (this.state.error !== undefined) {
      return <Error error_desc={this.state.error.message} />
    } else {
      return (
        <div className="loading">
          <strong>Loading {this.props.dataset_name}...</strong>
          <Progress animated color="success" value="100" />
        </div>
      )
    }
  }
}
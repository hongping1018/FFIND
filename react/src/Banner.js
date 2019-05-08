import React from 'react'
import {
  Container,
  Row,
  Col,
  Button
} from 'reactstrap'

import {
  Link
} from 'react-router-dom'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

import HomeModal from './HomeModal'

import Particles from 'react-particles-js'

import bannerImg from './assets/banner-bg3-fade.png'

import illustration from './assets/pancreas-islet-cells.png'

export default class Banner extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      modalOpen: false
    }
    this.toggle = this.toggle.bind(this)
  }

  toggle () {
    this.setState({
      modalOpen: !this.state.modalOpen
    })
  }

  render () {
    return (
      <div>
        <div className='overlay'>
          <Particles
            params={{
              particles: {
                number: {
                  value: 50,
                  density: {
                    enable: true,
                    value_area: 1600
                  }
                },
                color: {
                  value: '#ffffff'
                },
                shape: {
                  type: 'circle',
                  stroke: {
                    width: 0,
                    color: '#000000'
                  },
                  polygon: {
                    nb_sides: 5
                  },
                  image: {
                    src: 'img/github.svg',
                    width: 100,
                    height: 100
                  }
                },
                opacity: {
                  value: 0.5,
                  random: false,
                  anim: {
                    enable: false,
                    speed: 1,
                    opacity_min: 0.1,
                    sync: false
                  }
                },
                size: {
                  value: 10,
                  random: true,
                  anim: {
                    enable: false,
                    speed: 1,
                    size_min: 0.1,
                    sync: false
                  }
                },
                line_linked: {
                  enable: false,
                  distance: 150,
                  color: '#ffffff',
                  opacity: 0.4,
                  width: 1
                },
                move: {
                  enable: true,
                  speed: 2,
                  direction: 'top-right',
                  random: false,
                  straight: false,
                  out_mode: 'out',
                  bounce: false,
                  attract: {
                    enable: false,
                    rotateX: 600,
                    rotateY: 1200
                  }
                }
              },
              interactivity: {
                detect_on: 'window',
                events: {
                  onhover: {
                    enable: true,
                    mode: 'bubble'
                  },
                  onclick: {
                    enable: false,
                    mode: 'push'
                  },
                  resize: true
                },
                modes: {
                  grab: {
                    distance: 400,
                    line_linked: {
                      opacity: 1
                    }
                  },
                  bubble: {
                    distance: 400,
                    size: 12,
                    duration: 2,
                    opacity: 0.7,
                    speed: 3
                  },
                  repulse: {
                    distance: 200,
                    duration: 0.4
                  },
                  push: {
                    particles_nb: 4
                  },
                  remove: {
                    particles_nb: 2
                  }
                }
              },
              retina_detect: true
            }} style={{
              display: 'block',
              position: 'relative',
              zIndex: -1,
              width: '100%',
              height: '100%',
              background: `url(${bannerImg}) no-repeat center center fixed`,
              backgroundSize: 'cover'
            }}
            height={'90vh'}
          />
        </div>

        <Container className='banner-container'>
          <Row className='mt-4' style={{ height: '70%' }}>
            <Col md='6' className='align-self-center'>
              <h1 className='banner-header'>We study the human pancreas and islets from birth to adulthood.</h1>
              <h4 className='banner-subheader-left'>We are building a practical resource for assembling and sharing data from human pancreas samples.</h4>
              {/* <Link to='/datasets'><Button className='banner-btn'color='info'size='lg' block>View our Collections</Button></Link> */}
            </Col>
            <Col md='1' />
            <Col md='5' className='align-self-center d-none d-md-block'>
              <Row className='mt-3'>
                <div>
                  <Link to={'/datasets'} ><img src={illustration} responsive={'true'} alt='View our datasets' /></Link>
                </div>
              </Row>
            </Col>
          </Row>
          <Row className='mt-4' style={{ height: '15%' }}>
            <Col md='6'>
              <Link to={'/datasets'}><Button className='banner-btn' color='info' size='lg' block>View Our Collections</Button></Link>
            </Col>
            <Col md='6'>
              <Link to={'/about'}><Button className='banner-btn' color='secondary' size='lg' block>Learn About pancreatlas</Button></Link>
            </Col>
          </Row>
          <Row className='mb-1' style={{ height: '10%' }}>
            <Col md='12' className='text-center'>
              <FontAwesomeIcon className='scroll-down-arrow' onClick={this.props.scrollDown} icon='angle-down' size='6x' color='white' />
            </Col>
          </Row>
          <HomeModal isOpen={this.state.modalOpen} toggle={this.toggle} />
        </Container>
      </div>
    )
  }
}

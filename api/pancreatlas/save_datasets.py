import json
import api.omero_api as api

def save_datasets():
    dsets = api.get_datasets()
    dids = [384, 390]
    for did in dids:
        print "Saving %s" % (str(did),)
        fname = "/app001/www/assets/pancreatlas/datasets/%s.txt" % (str(did), )
        print fname
        ids = {}
        images = api.get_images_from_dataset(did)
#        images = dset.imgs
        f = open(fname, 'w')
        for image in images:
            ids[int(image.id)] = [tag.tname for tag in image.get_tags()]
        data = json.dumps(ids)
        f.write(data)
        f.close() 

def save_index():
    print 'Retrieving images'
    imgs = api.get_images_from_dataset(384)
    print 'Images retrieved'
    img_dict = {}
    POSSIBLE_TAGS = ['INS', 'COL4A1', 'SST', 'PECAM1', 'PTF1A', 'CPA1', 'FOXA2', 'AMY1A', 'GP2', 'NKX6-1', 'PAX6', 'SYP', 'GCG', 'PPY', 'MK167', 'SYN1', 'SYN2', 'Ki67', 'SOX9', 'AMY1A', 'ONECUT1', 'HNF1B', 'PAX6', 'GP2', 'NKX6-1', 'PTF1A', 'NEUROG3', 'GHRL', 'CDH1']
    for img in imgs:
        print img.id
        tags = [tag.tname for tag in img.get_tags()]
        if set(tags).isdisjoint(POSSIBLE_TAGS) and 'macro image' not in img.name and 'label image' not in img.name:
            print 'WARNING: Double check import for image %s' % (img.id,)
        img_dict[str(img.id)] = [tags]

    f = open('/app001/www/assets/pancreatlas/datasets/image_index.txt', 'w')
    f.write(json.dumps(img_dict))
    f.close
    
def main():
    save_datasets()

if __name__=='__main__':
    main()

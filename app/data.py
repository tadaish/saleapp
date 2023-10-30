def get_categories():
    return [{
                'id': 1,
                'name': 'Mobile'
            },
            {
                'id': 2,
                'name': 'Tablet'
            }]


def get_products(kw):
    products = [{
        'id':1,
        'name':"Iphone 14",
        'price': 20000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2022/09/08/anh-chup-man-hinh-2022-09-08-luc-01-59-18-removebg-preview.png",
        "category_id": 1
    }, {
        'id':2,
        'name':"Samsung Galaxy S24 Plus",
        'price': 20000000,
        "image": "https://cdn2.cellphones.com.vn/x/media/catalog/product/f/b/fbhgngh_2_.jpg",
        "category_id": 1
    }, {
        'id':3,
        'name':"Iphone 14",
        'price': 20000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2022/09/08/anh-chup-man-hinh-2022-09-08-luc-01-59-18-removebg-preview.png",
        "category_id": 1
    }, {
        'id':4,
        'name':"Iphone 14",
        'price': 20000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2022/09/08/anh-chup-man-hinh-2022-09-08-luc-01-59-18-removebg-preview.png",
        "category_id": 1
    }, {
        'id':5,
        'name':"Iphone 14",
        'price': 20000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2022/09/08/anh-chup-man-hinh-2022-09-08-luc-01-59-18-removebg-preview.png",
        "category_id": 1
    }, {
        'id':6,
        'name':"Iphone 14",
        'price': 20000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2022/09/08/anh-chup-man-hinh-2022-09-08-luc-01-59-18-removebg-preview.png",
        "category_id": 1
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >=0]

    return products
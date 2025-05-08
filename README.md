# gotit-api-python-sdk
SDK Technical document for GotIt APIs

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Dayone-Joint-Stock-Company/gotit-api-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Dayone-Joint-Stock-Company/gotit-api-python-sdk.git`)

Then import the package:
```python
import gotit_api_python_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gotit_api_python_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import gotit_api_python_sdk
from gotit_api_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-biz-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = gotit_api_python_sdk.Configuration(
    host = "https://api-biz-stg.gotit.vn"
)



# Enter a context with an instance of the API client
with gotit_api_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gotit_api_python_sdk.BrandsApi(api_client)
    x_gi_authorization = 'API key GotIt provided' # str | Authorization

    try:
        # Get brand by product
        api_response = api_instance.brands_by_products(x_gi_authorization)
        print("The response of BrandsApi->brands_by_products:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BrandsApi->brands_by_products: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api-biz-stg.gotit.vn*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrandsApi* | [**brands_by_products**](docs/BrandsApi.md#brands_by_products) | **GET** /api/v4.0/brands/brandsByProducts | Get brand by product
*BrandsApi* | [**get_detail_of_brand**](docs/BrandsApi.md#get_detail_of_brand) | **GET** /api/v4.0/brands/{id} | Get brand detail
*BrandsApi* | [**get_list_of_brands**](docs/BrandsApi.md#get_list_of_brands) | **GET** /api/v4.0/brands | Get list of brands
*CategoriesApi* | [**get_category_by_product**](docs/CategoriesApi.md#get_category_by_product) | **GET** /api/v4.0/categories/categoriesByProducts | Get category by product
*CategoriesApi* | [**get_list_of_categories**](docs/CategoriesApi.md#get_list_of_categories) | **GET** /api/v4.0/categories | Get lists category
*ProductsApi* | [**get_list_of_products**](docs/ProductsApi.md#get_list_of_products) | **GET** /api/v4.0/products | Get all products master data
*ProductsApi* | [**get_product_detail**](docs/ProductsApi.md#get_product_detail) | **GET** /api/v4.0/products/{id} | Get product detail data
*ProductsApi* | [**get_stores_of_product**](docs/ProductsApi.md#get_stores_of_product) | **GET** /api/v4.0/products/{id}/stores | Get stores of this product
*VoucherApi* | [**create_voucher_link_e**](docs/VoucherApi.md#create_voucher_link_e) | **POST** /api/v4.0/vouchers/e | Create voucher link e
*VoucherApi* | [**create_voucher_link_g**](docs/VoucherApi.md#create_voucher_link_g) | **POST** /api/v4.0/vouchers/g | Create voucher link g
*VoucherApi* | [**create_voucher_link_v**](docs/VoucherApi.md#create_voucher_link_v) | **POST** /api/v4.0/vouchers/v | Create voucher link v
*VoucherSendMethodApi* | [**check_status_zns**](docs/VoucherSendMethodApi.md#check_status_zns) | **POST** /api/v4.0/vouchers/send/zns/check | Check status zns
*VoucherSendMethodApi* | [**send_voucher_by_email**](docs/VoucherSendMethodApi.md#send_voucher_by_email) | **POST** /api/v4.0/vouchers/send/email | Send voucher by mail
*VoucherSendMethodApi* | [**send_voucher_by_sms**](docs/VoucherSendMethodApi.md#send_voucher_by_sms) | **POST** /api/v4.0/vouchers/send/sms | Send voucher by sms
*VoucherSendMethodApi* | [**send_voucher_by_zns**](docs/VoucherSendMethodApi.md#send_voucher_by_zns) | **POST** /api/v4.0/vouchers/send/zns | Send voucher by zns
*VoucherStatusApi* | [**check_voucher**](docs/VoucherStatusApi.md#check_voucher) | **GET** /api/v4.0/vouchers/multiple/status/{refId} | Check voucher status


## Documentation For Models

 - [BRANDCATEGORYDETAIL](docs/BRANDCATEGORYDETAIL.md)
 - [BRANDCATEGORYDETAILRESPONSE](docs/BRANDCATEGORYDETAILRESPONSE.md)
 - [BRANDDETAIL](docs/BRANDDETAIL.md)
 - [BRANDDETAILRESPONSE](docs/BRANDDETAILRESPONSE.md)
 - [BRANDREEDEMSCHEMA](docs/BRANDREEDEMSCHEMA.md)
 - [BRANDSDETAIL](docs/BRANDSDETAIL.md)
 - [BRANDSRESPONSE](docs/BRANDSRESPONSE.md)
 - [CATEGORIESDETAIL](docs/CATEGORIESDETAIL.md)
 - [CATEGORIESRESPONSE](docs/CATEGORIESRESPONSE.md)
 - [GROUPVOUCHERSCHEMA](docs/GROUPVOUCHERSCHEMA.md)
 - [HTTPBADREQUEST](docs/HTTPBADREQUEST.md)
 - [HTTPINTERNALSERVERERROR](docs/HTTPINTERNALSERVERERROR.md)
 - [HTTPNOTFOUND](docs/HTTPNOTFOUND.md)
 - [HTTPUNAUTHORIZED](docs/HTTPUNAUTHORIZED.md)
 - [PAGINGSCHEMA](docs/PAGINGSCHEMA.md)
 - [PRODUCTDEFAULTLINKG](docs/PRODUCTDEFAULTLINKG.md)
 - [PRODUCTDETAIL](docs/PRODUCTDETAIL.md)
 - [PRODUCTDETAILRESPONSE](docs/PRODUCTDETAILRESPONSE.md)
 - [PRODUCTG](docs/PRODUCTG.md)
 - [PRODUCTPRICESCHEMA](docs/PRODUCTPRICESCHEMA.md)
 - [PRODUCTSALLDETAIL](docs/PRODUCTSALLDETAIL.md)
 - [PRODUCTSDEFAULTLINKG](docs/PRODUCTSDEFAULTLINKG.md)
 - [PRODUCTSDETAIL](docs/PRODUCTSDETAIL.md)
 - [PRODUCTSRESPONSE](docs/PRODUCTSRESPONSE.md)
 - [PRODUCTSRESPONSEDataInner](docs/PRODUCTSRESPONSEDataInner.md)
 - [PRODUCTSVOUCHERCHECK](docs/PRODUCTSVOUCHERCHECK.md)
 - [PRODUCTV](docs/PRODUCTV.md)
 - [PRODUCTVENDORLINKG](docs/PRODUCTVENDORLINKG.md)
 - [REQUESTCHECKSTATUSZNS](docs/REQUESTCHECKSTATUSZNS.md)
 - [REQUESTCREATEVOUCHERLINKE](docs/REQUESTCREATEVOUCHERLINKE.md)
 - [REQUESTCREATEVOUCHERLINKG](docs/REQUESTCREATEVOUCHERLINKG.md)
 - [REQUESTCREATEVOUCHERLINKV](docs/REQUESTCREATEVOUCHERLINKV.md)
 - [REQUESTSENDVOUCHERBYEMAIL](docs/REQUESTSENDVOUCHERBYEMAIL.md)
 - [REQUESTSENDVOUCHERBYSMS](docs/REQUESTSENDVOUCHERBYSMS.md)
 - [REQUESTSENDVOUCHERBYZNS](docs/REQUESTSENDVOUCHERBYZNS.md)
 - [STOREPAGINGSCHEMA](docs/STOREPAGINGSCHEMA.md)
 - [STOREPRODUCTSCHEMA](docs/STOREPRODUCTSCHEMA.md)
 - [STORESRESPONSE](docs/STORESRESPONSE.md)
 - [STORESRESPONSEDataInner](docs/STORESRESPONSEDataInner.md)
 - [STORESSCHEMA](docs/STORESSCHEMA.md)
 - [USAGEMETHODSCHEMA](docs/USAGEMETHODSCHEMA.md)
 - [VENDORSCHEMA](docs/VENDORSCHEMA.md)
 - [VOUCHERCHECKRESPONSE](docs/VOUCHERCHECKRESPONSE.md)
 - [VOUCHERCHECKSCHEMA](docs/VOUCHERCHECKSCHEMA.md)
 - [VOUCHERCHECKSCHEMADETAIL](docs/VOUCHERCHECKSCHEMADETAIL.md)
 - [VOUCHERCHECKZNSRESPONSE](docs/VOUCHERCHECKZNSRESPONSE.md)
 - [VOUCHERCHECKZNSRESPONSEData](docs/VOUCHERCHECKZNSRESPONSEData.md)
 - [VOUCHERE](docs/VOUCHERE.md)
 - [VOUCHERERESPONSE](docs/VOUCHERERESPONSE.md)
 - [VOUCHERESCHEMA](docs/VOUCHERESCHEMA.md)
 - [VOUCHERG](docs/VOUCHERG.md)
 - [VOUCHERGRESPONSE](docs/VOUCHERGRESPONSE.md)
 - [VOUCHERGSCHEMA](docs/VOUCHERGSCHEMA.md)
 - [VOUCHERSENDEMAILRESPONSE](docs/VOUCHERSENDEMAILRESPONSE.md)
 - [VOUCHERSENDEMAILSCHEMA](docs/VOUCHERSENDEMAILSCHEMA.md)
 - [VOUCHERSENDSMSRESPONSE](docs/VOUCHERSENDSMSRESPONSE.md)
 - [VOUCHERSENDSMSSCHEMA](docs/VOUCHERSENDSMSSCHEMA.md)
 - [VOUCHERSENDZNSRESPONSE](docs/VOUCHERSENDZNSRESPONSE.md)
 - [VOUCHERSENDZNSRESPONSEData](docs/VOUCHERSENDZNSRESPONSEData.md)
 - [VOUCHERV](docs/VOUCHERV.md)
 - [VOUCHERVRESPONSE](docs/VOUCHERVRESPONSE.md)
 - [VOUCHERVSCHEMA](docs/VOUCHERVSCHEMA.md)
 - [VOUCHERVSCHEMAProduct](docs/VOUCHERVSCHEMAProduct.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

quang.huynh@gotit.vn

## Running Examples with Docker

The SDK includes example applications in the `example` directory that demonstrate various API functionalities. You can run these examples using Docker:

1. Make sure you have Docker and Docker Compose installed on your system
2. Navigate to the example directory:
```bash
cd example
```

3. Build and run the example application:
```bash
docker-compose up --build
```

The example application will be available at `http://localhost:5000`
### Available Endpoints

#### Voucher Endpoints
- `GET /vouchers/e` - Create E voucher
- `GET /vouchers/v` - Create V voucher
- `GET /vouchers/g` - Create G voucher
- `GET /vouchers/send_sms` - Send voucher via SMS
- `GET /vouchers/send_email` - Send voucher via Email
- `GET /vouchers/send_zns` - Send voucher via ZNS
- `GET /vouchers/check_zns` - Check ZNS status
- `GET /vouchers/check_status_voucher` - Check voucher status

#### Brand Endpoints
- `GET /brands` - List all brands
- `GET /brands/{id}` - Get brand details
- `GET /brands/brand_product` - Get brand products

#### Category Endpoints
- `GET /categories` - List all categories
- `GET /categories/category_product` - Get category products

#### Product Endpoints
- `GET /products` - List all products
- `GET /products/{id}` - Get product details
- `GET /products/{id}/stores` - Get product stores

The example directory structure:
```
example/
├── app.py              # Main application entry point
├── config.py           # Configuration settings
├── routes.py           # API route definitions
├── utils.py            # Utility functions
├── services/           # Service implementations
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
└── requirements.txt    # Example application dependencies
```

For more details about the example implementation, please refer to the files in the `example` directory.



from flask import Blueprint, jsonify
from gotit_api_python_sdk.api import (
    brands_api,
    categories_api,
    products_api,
    voucher_api,
    voucher_send_method_api,
    voucher_status_api
)
from gotit_api_python_sdk.models.requestcreatevoucherlinke import REQUESTCREATEVOUCHERLINKE
from gotit_api_python_sdk.models.requestcreatevoucherlinkv import REQUESTCREATEVOUCHERLINKV
from gotit_api_python_sdk.models.requestcreatevoucherlinkg import REQUESTCREATEVOUCHERLINKG
from gotit_api_python_sdk.models.requestsendvoucherbysms import REQUESTSENDVOUCHERBYSMS
from gotit_api_python_sdk.models.requestsendvoucherbyemail import REQUESTSENDVOUCHERBYEMAIL
from gotit_api_python_sdk.models.requestsendvoucherbyzns import REQUESTSENDVOUCHERBYZNS
from gotit_api_python_sdk.models.requestcheckstatuszns import REQUESTCHECKSTATUSZNS
from gotit_api_python_sdk.models.productdefaultlinkg import PRODUCTDEFAULTLINKG
from services.api_client import GotItAPIClient
from utils import load_private_key_from_string, sign_data, generate_random_string
from config import Config

app_routes = Blueprint("app_routes", __name__)
api_client = GotItAPIClient()

# Brand APIs
@app_routes.route("/brands", methods=['GET'])
def brands():
    with api_client.get_client() as client:
        api_instance = brands_api.BrandsApi(client)
        try:
            api_response = api_instance.get_list_of_brands(api_client.get_authorization())
            return jsonify(api_response.to_dict())
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/brands/<int:brand_id>", methods=['GET'])
def brand_detail(brand_id):
    with api_client.get_client() as client:
        api_instance = brands_api.BrandsApi(client)
        try:
            api_response = api_instance.get_detail_of_brand(api_client.get_authorization(), brand_id)
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/brands/brand_product", methods=['GET'])
def brand_product():
    with api_client.get_client() as client:
        api_instance = brands_api.BrandsApi(client)
        try:
            api_response = api_instance.brands_by_products(api_client.get_authorization())
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Category APIs
@app_routes.route("/categories", methods=['GET'])
def categories():
    with api_client.get_client() as client:
        api_instance = categories_api.CategoriesApi(client)
        try:
            api_response = api_instance.get_list_of_categories(api_client.get_authorization())
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/categories/category_product", methods=['GET'])
def category_product():
    with api_client.get_client() as client:
        api_instance = categories_api.CategoriesApi(client)
        try:
            api_response = api_instance.get_category_by_product(api_client.get_authorization())
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Product APIs
@app_routes.route("/products", methods=['GET'])
def products():
    with api_client.get_client() as client:
        api_instance = products_api.ProductsApi(client)
        try:
            api_response = api_instance.get_list_of_products(
                api_client.get_authorization(),
                Config.DEFAULT_PAGE,
                Config.DEFAULT_PAGE_SIZE,
                min_price=Config.DEFAULT_MIN_PRICE,
                max_price=Config.DEFAULT_MAX_PRICE,
                is_exclude_store_list_info=False,
                store_list_page=Config.DEFAULT_STORE_PAGE,
                store_list_page_size=Config.DEFAULT_STORE_PAGE_SIZE
            )
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/products/<int:product_id>", methods=['GET'])
def product_detail(product_id):
    with api_client.get_client() as client:
        api_instance = products_api.ProductsApi(client)
        try:
            api_response = api_instance.get_product_detail(
                api_client.get_authorization(),
                product_id,
                is_exclude_store_list_info=False,
                store_list_page=Config.DEFAULT_STORE_PAGE,
                store_list_page_size=Config.DEFAULT_STORE_PAGE_SIZE
            )
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/products/<int:product_id>/stores", methods=['GET'])
def product_store(product_id):
    with api_client.get_client() as client:
        api_instance = products_api.ProductsApi(client)
        try:
            api_response = api_instance.get_stores_of_product(api_client.get_authorization(), product_id)
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Voucher APIs
@app_routes.route("/vouchers/e", methods=['GET'])
def generate_vouchers_e():
    with api_client.get_client() as client:
        api_instance = voucher_api.VoucherApi(client)
        try:
            order_name = generate_random_string()
            transaction_ref_id = generate_random_string()
            data = api_client.get_authorization() + "|" + transaction_ref_id
            private_key = load_private_key_from_string()
            signature = sign_data(private_key, data)
            
            request_create_voucher_link_e = REQUESTCREATEVOUCHERLINKE(
                order_name=order_name,
                transaction_ref_id=transaction_ref_id,
                amount=100000,
                expiry_date="2025-11-15",
                product_id=1541,
                use_otp=1,
                otp_type=1,
                password="123456",
                receiver_name="Quang Huynh",
                phone="0394162063",
                email="quang.huynh@gotit.vn",
                signature=signature
            )

            api_response = api_instance.create_voucher_link_e(
                api_client.get_authorization(),
                requestcreatevoucherlinke=request_create_voucher_link_e
            )
            return jsonify(api_response.to_dict())
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/vouchers/v", methods=['GET'])
def generate_vouchers_v():
    with api_client.get_client() as client:
        api_instance = voucher_api.VoucherApi(client)
        try:
            order_name = generate_random_string()
            transaction_ref_id = generate_random_string()
            request_create_voucher_link_v = REQUESTCREATEVOUCHERLINKV(
                product_id=1541,
                product_price_id=2991,
                quantity=1,
                order_name=order_name,
                expiry_date="2025-11-15",
                transaction_ref_id=transaction_ref_id,
                use_otp=1,
                otp_type=1,
                password="123456",
                receiver_name="Quang Huynh",
                phone="0394162063",
                email="quang.huynh@gotit.vn",
                active_date="",
                is_convert_to_cover_link=1,
            )
            api_response = api_instance.create_voucher_link_v(
                api_client.get_authorization(),
                requestcreatevoucherlinkv=request_create_voucher_link_v
            )
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/vouchers/g", methods=['GET'])
def generate_vouchers_g():
    with api_client.get_client() as client:
        api_instance = voucher_api.VoucherApi(client)
        try:
            order_name = generate_random_string()
            transaction_ref_id = generate_random_string()
            request_create_voucher_link_g = REQUESTCREATEVOUCHERLINKG(
                product_list=[
                    PRODUCTDEFAULTLINKG(
                        product_id=1541,
                        product_price_id=2991,
                        quantity=1,
                    ),
                ],
                order_name=order_name,
                expiry_date="2025-11-15",
                transaction_ref_id=transaction_ref_id,
                use_otp=1,
                otp_type=1,
                password="123456",
                receiver_name="Quang Huynh",
                phone="0394162063",
                email="quang.huynh@gotit.vn",
            )
            api_response = api_instance.create_voucher_link_g(
                api_client.get_authorization(),
                requestcreatevoucherlinkg=request_create_voucher_link_g
            )
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Voucher Send Method APIs
@app_routes.route("/vouchers/send_sms", methods=['GET'])
def send_voucher_sms():
    with api_client.get_client() as client:
        api_instance = voucher_send_method_api.VoucherSendMethodApi(client)
        try:
            request_send_voucher_by_sms = REQUESTSENDVOUCHERBYSMS(
                voucher_link_code="gLsZaFRN",
                phone_no="0394162063",
                receiver_nm="Got It",
                sender_nm="Got It",
            )
            api_response = api_instance.send_voucher_by_sms(
                api_client.get_authorization(),
                requestsendvoucherbysms=request_send_voucher_by_sms
            )
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/vouchers/send_email", methods=['GET'])
def send_voucher_email():
    with api_client.get_client() as client:
        api_instance = voucher_send_method_api.VoucherSendMethodApi(client)
        try:
            request_send_voucher_by_email = REQUESTSENDVOUCHERBYEMAIL(
                voucher_link_code="gLsZaFRN",
                email="quang.huynh@gotit.vn",
                receiver_nm="Got It",
                sender_nm="Got It",
                message="Have a good day",
            )
            api_response = api_instance.send_voucher_by_email(
                api_client.get_authorization(),
                requestsendvoucherbyemail=request_send_voucher_by_email
            )
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/vouchers/send_zns", methods=['GET'])
def send_voucher_zns():
    with api_client.get_client() as client:
        api_instance = voucher_send_method_api.VoucherSendMethodApi(client)
        try:
            transaction_id = generate_random_string(15)
            request_send_voucher_by_zns = REQUESTSENDVOUCHERBYZNS(
                phone_no="0394162063",
                receiver_nm="Got It",
                voucher_serials=["E2V2RML6F52"],
                transaction_id=transaction_id,
            )
            api_response = api_instance.send_voucher_by_zns(
                api_client.get_authorization(),
                requestsendvoucherbyzns=request_send_voucher_by_zns
            )
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/vouchers/check_zns", methods=['GET'])
def check_status_zns():
    with api_client.get_client() as client:
        api_instance = voucher_send_method_api.VoucherSendMethodApi(client)
        try:
            request_check_status_zns = REQUESTCHECKSTATUSZNS(
                transaction_id='aNGqaAljTaLc5B3',
            )
            api_response = api_instance.check_status_zns(
                api_client.get_authorization(),
                requestcheckstatuszns=request_check_status_zns
            )
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app_routes.route("/vouchers/check_status_voucher", methods=['GET'])
def check_status_voucher():
    with api_client.get_client() as client:
        api_instance = voucher_status_api.VoucherStatusApi(client)
        try:
            ref_id = "1111_1aa11"
            api_response = api_instance.check_voucher(
                api_client.get_authorization(),
                ref_id,
                is_exclude_store_list_info=False,
                store_list_page=Config.DEFAULT_STORE_PAGE,
                store_list_page_size=Config.DEFAULT_STORE_PAGE_SIZE
            )
            if hasattr(api_response, "to_dict"):
                return jsonify(api_response.to_dict())
            return jsonify(api_response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

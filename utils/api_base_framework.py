from playwright.sync_api import Playwright

orders_payload = {
    "orders": [
        {
            "country": "Indonesia",
            "productOrderedId": "67a8df1ac0d3e6622a297ccb"
        }
    ]
}

class APIutils:

    def get_token(self, playwright: Playwright, user_credentials):
        user_email = user_credentials["userEmail"]
        user_password = user_credentials["userPassword"]

        api_request_context = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )

        response = api_request_context.post(
            "/api/ecom/auth/login",
            data={"userEmail": user_email, "userPassword": user_password}
        )

        assert response.ok
        response_body = response.json()
        return response_body["token"] # Returns auth token

    def create_order(self, playwright: Playwright, user_credentials):
        token = self.get_token(playwright, user_credentials)

        api_request_context = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )

        response = api_request_context.post(
            "/api/ecom/order/create-order",
            data=orders_payload,
            headers={
                "authorization": token,
                "content-type": "application/json"
            }
        )

        response_body = response.json()
        response_order_id = response_body["orders"][0]
        return response_order_id # Returns order ID

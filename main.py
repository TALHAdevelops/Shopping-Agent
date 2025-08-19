from agents import Agent, Runner, function_tool
import requests
from connection import config

API_URLS = [
    "https://hackathon-apis.vercel.app/api/products",
    "https://template-03-api.vercel.app/api/products",
    "https://next-ecommerce-template-4.vercel.app/api/product",
    "https://template6-six.vercel.app/api/products",
]

@function_tool
def shopping_data():
    """Fetch product data from multiple APIs"""
    all_data = []
    for url in API_URLS:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                # some APIs return dict with "products", normalize to list
                if isinstance(data, dict) and "products" in data:
                    data = data["products"]
                elif isinstance(data, dict) and "product" in data:
                    data = data["product"]
                if isinstance(data, list):
                    all_data.extend(data)
                else:
                    all_data.append(data)
        except Exception as e:
            all_data.append({"error": f"Failed to fetch from {url}", "details": str(e)})
    return all_data

Assistant = Agent(
    name="Shopping Assistant",
    instructions=(
        "You are a helpful assistant and shopping expert. "
        "Always call your tools to get data before answering."
    ),
    tools=[shopping_data]
)

User_query = input("Enter your query: ")

def main():
    res = Runner.run_sync(
        Assistant,
        User_query,
        run_config=config,
    )
    print(res.final_output)

if __name__ == "__main__":
    main()

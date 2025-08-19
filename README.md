🛒 Shopping Agent

A simple Python project that works like a shopping helper.
It collects product data from many online store APIs and gives results in one place.

✨ Features

Gets products from many APIs.

Handles errors if a site does not respond.

Uses a smart agent that always calls the right tool.

Easy to run with one command.

📂 Project Structure
Shopping-Agent/
│
├── main.py          # Main file to run the agent
├── agents/          # Contains Agent, Runner, and helper tools
├── connection.py    # Holds config details
├── pyproject.toml   # Project setup and dependencies
└── README.md        # Project guide

⚙️ Setup

Clone the repo

git clone https://github.com/TALHAdevelops/Shopping-Agent.git
cd Shopping-Agent


Install requirements
(If you use uv, you can do: uv sync)
Or with pip:

pip install -r requirements.txt

▶️ Usage

Run the main file:

python main.py


Enter your question (like "Show me products").
The agent will fetch data from these APIs:

https://hackathon-apis.vercel.app/api/products

https://template-03-api.vercel.app/api/products

https://next-ecommerce-template-4.vercel.app/api/product

https://template6-six.vercel.app/api/products

📊 Example Output
Enter your query: show me products
[ { "id": 1, "name": "Shoes", "price": 50 }, ... ]

🔧 Notes

If an API fails, it will show an error message.

You can add more API links inside API_URLS in main.py.

🤝 Contributing

Pull requests are welcome. For big changes, please open an issue first.

📩 Contact

Made by M. Talha
GitHub Profile

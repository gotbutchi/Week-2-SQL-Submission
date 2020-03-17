import sqlite3


class Database:
    def __init__(self, name: str = 'tiki.db'):
        self.conn = sqlite3.connect(name)
        self._create_category_table()
        self._create_product_table()

    def __del__(self):
        # For each class there will be a deinit or destructor.
        self.conn.commit()
        self.conn.close()

    def _create_category_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS category (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255),
                url TEXT, 
                parent_id INT, 
                create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """

        self.conn.execute(query)

    def _create_product_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255),
                url TEXT,
                img_url TEXT,
                regular_price TEXT,
                final_price TEXT,            
                sale_tag TEXT,
                comment INT,
                rating TEXT,
                cat_id INT,
                FOREIGN KEY(cat_id) REFERENCES categories(parent_id)
                );
        """

        self.conn.execute(query)

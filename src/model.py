import sqlite3
from json import dumps


class Category():
    def __init__(self, cat_id, name, url, parent_id):
        self.conn = sqlite3.connect('tiki.db')
        self.conn.row_factory = sqlite3.Row
        self.cat_id = cat_id
        self.name = name
        self.url = url
        self.parent_id = parent_id
        self.table_name = "category"

    def __repr__(self):
        return dumps(self.__dict__)

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def _get_by_id(self, _id):
        pass

    def create(self):
        query = f"""
            INSERT INTO {self.table_name} (
                name,
                url,
                parent_id
            )
            VALUES (?, ?, ?);
        """

        val = (
            self.name,
            self.url,
            self.parent_id
        )

        self.conn.execute(query, val)
    
    def update(self):
        pass

    def delete(self):
        pass

    def read(self, _id = None):
        query = f"""
        SELECT * FROM {self.table_name}
        """
        if _id is not None:
            query += f"WHERE id={_id}"

        result_set = self.conn.execute(query).fetchall()
        return [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
            for row in result_set
        ]


class Product():
    # Too many arguments
    def __init__(
        self,
        product_id,
        name,
        url,
        image_url,
        regular_price,
        final_price,
        sale_tag,
        comment,
        rating,
        cat_id
    ):
        self.conn = sqlite3.connect('tiki.db')
        self.conn.row_factory = sqlite3.Row
        self.product_id = product_id
        self.name = name
        self.url = url
        self.image_url = image_url
        self.regular_price = regular_price
        self.final_price = final_price
        self.sale_tag = sale_tag
        self.comment = comment
        self.rating = rating
        self.cat_id = cat_id

    def __repr__(self):
        return dumps(self.__dict__)

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create(self):
        query = """
            INSERT INTO product (name, url, img_url, regular_price, final_price, sale_tag, comment, rating, cat_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        val = (self.name, self.url, self.img_url, self.regular_price, self.final_price, self.sale_tag, self.comment, self.rating, self.cat_id)
        self.conn.execute(query, val)

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
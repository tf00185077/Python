// 商品類別（OOP）
class Item {
    constructor(name, price) {
        this.name = name;
        this.price = price;
    }
}

// 購物車函數（FP）
const createShoppingCart = () => {
    const items = [];

    const addItem = (item) => {
        items.push(item);
    };

    const getTotal = () => {
        return items.reduce((total, item) => total + item.price, 0);
    };

    return { addItem, getTotal };
};

// 使用混和的示例
const item1 = new Item("商品1", 10);
const item2 = new Item("商品2", 20);

const cart = createShoppingCart();
cart.addItem(item1);
cart.addItem(item2);

console.log("總計：", cart.getTotal()); // 總計：30

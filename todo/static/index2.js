let goods = {
    "apricot": 1,
    "blueberry": 1,
    "pear": 1,
    "cherry": 1,
    "mashrooms": 1,
    "pistachio": 1,
    "fig": 1,
    "granat": 1

};

document.onclick = event => {
    if (event.target.classList.contains("plus")) {
        //console.log(event.target.dataset.id);
        plusFunction(event.target.dataset.id);
    }
    if (event.target.classList.contains("minus")) {
        minusFunction(event.target.dataset.id);
    }
}
//увеличение кол-ва товарва
const plusFunction = id => {
    //console.log(goods);
    goods[id]++;
    renderGoods();
}

//уменьшение товара
const minusFunction = id => {
    if (goods[id] - 1 == 0) {
        deleteFunction(id);
        return true;
    }
    goods[id]--;
    renderGoods();
}
//удаление товара
const deleteFunction = id => {
    delete goods[id];
    renderGoods();
}

const renderGoods = () => {
    console.log(goods);
}

renderGoods();




function save() {

}

function itogo() {

}



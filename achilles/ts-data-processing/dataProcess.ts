type DataType = {
    key: string;
    value: string[];
    saved: string[];
};

let data: DataType[] = [
    {
        key: '1',
        value: ['Apple', 'Banana', 'Cherry'],
        saved: []
    },
    {
        key: '2',
        value: ['Dog', 'Elephant', 'Frog'],
        saved: []
    },
    {
        key: '2',
        value: ['Dog', 'Elephant', 'Frog'],
        saved: []
    }
];

function onSaved(key: string, label: string) {
    const obj = new Map(data.map((item) => [item.key, item]));

    const item = obj.get(key);

    if (!item) {
        return;
    }

    const savedSet = new Set(item.saved);

    if (item.value.includes(label)) {
        savedSet.add(label);
        item.value.splice(item.value.indexOf(label), 1);
    } else {
        item.value.push(label);
        savedSet.delete(label);
    }

    item.saved = Array.from(savedSet);

}

onSaved("3", "Apple");
console.log(data);
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

var FirstUnique = function(nums) {
    this.processed = {};
    this.head = null;
    this.tail = null;
    for (v of nums) {this.add(v);}
};

FirstUnique.prototype.showFirstUnique = function() {
    if (this.head) {return this.head.value;}
    return -1;
};

FirstUnique.prototype.remove = function(node) {
    if (node === this.head && node == this.tail) {
        this.head = this.tail = node = null;
        return;
    }
    if (node !== this.head && node !== this.tail) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    } else if (node == this.head){
        this.head = this.head.next;
        if (this.head) {this.head.prev = null;}
    } else {
        this.tail = this.tail.prev;
        this.tail.next = null;
    }
    node.next = null;
    node.prev = null;
};

FirstUnique.prototype.add = function(value) {
    if (value in this.processed) {
        if (this.processed[value] instanceof Node) {
            this.remove(this.processed[value]);
            this.processed[value] = null;
        }
    } else {
        const n = new Node(value);
        this.processed[value] = n;
        if (this.tail) {
            this.tail.next = n;
            n.prev = this.tail;
            this.tail = n;
        } else {
            this.head = this.tail = n;
        }
    }
};

t = new FirstUnique([2,3,5])
console.log("2 = ", t.showFirstUnique())
t.add(5)
console.log("2 = ", t.showFirstUnique())
t.add(2)
console.log("3 = ", t.showFirstUnique())
t.add(3)
console.log("-1 = ", t.showFirstUnique())

t = new FirstUnique([233])
console.log("233 = ", t.showFirstUnique())
t.add(11)
console.log("233 = ", t.showFirstUnique())
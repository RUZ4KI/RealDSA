class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  insert_at_head(value) {
    const new_node = new Node(value);
    new_node.next = this.head;
    this.head = new_node;
    if (this.size === 0) {
      this.tail = new_node;
    }
    this.size += 1;
  }

  insert_at_tail(value) {
    const new_node = new Node(value);
    if (this.size == 0) {
      this.head = new_node;
      this.tail = new_node;
      this.size += 1;
      return;
    }
    this.tail.next = new_node;
    this.tail = new_node;
    this.size += 1;
  }

  search(value) {
    let current = this.head;
    while (current !== null) {
      if (current.value === value) {
        return current;
      }
      current = current.next;
    }
    return null;
  }

  delete(value) {
    if (this.head === null) {
      return null;
    }
    if (this.head.value === value) {
      this.head = this.head.next;
      if (this.head === null) {
        this.tail = null;
      }
      this.size -= 1;
      return;
    }
    let prev = this.head;
    let curr = this.head.next;
    while (curr !== null) {
      if (curr.value === value) {
        prev.next = curr.next;
        if (curr === this.tail) {
          this.tail = prev;
        }
        this.size -= 1;
        return;
      }
      prev = curr;
      curr = curr.next;
    }
  }
}

const list = new SinglyLinkedList();

list.insert_at_head(10);
list.insert_at_tail(30);
list.search(99);
list.delete(10);

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  insert_at_head(value) {
    const new_node = new Node(value);
    new_node.next = this.head;

    if (this.head !== null) {
      this.head.prev = new_node;
    }

    this.head = new_node;

    if (this.size === 0) {
      this.tail = new_node;
    }
    this.size += 1;
  }

  insert_at_tail(value) {
    const new_node = new Node(value);
    new_node.prev = this.tail;

    if (this.tail !== null) {
      this.tail.next = new_node;
    }

    this.tail = new_node;

    if (this.size === 0) {
      this.head = new_node;
    }
    this.size += 1;
  }

  search(value) {
    let curr = this.head;
    while (curr) {
      if (curr.value === value) {
        return true;
      }
      curr = curr.next;
    }
    return false;
  }

  delete(value) {
    if (this.head === null) {
      return;
    }

    if (this.head.value === value) {
      this.head = this.head.next;
      if (this.head !== null) {
        this.head.prev = null;
      } else {
        this.tail = null;
      }
      this.size -= 1;
      return;
    }

    let curr = this.head;
    while (curr) {
      if (curr.value === value) {
        let prev_node = curr.prev;
        let next_node = curr.next;
        if (prev_node !== null) {
          prev_node.next = next_node;
        }
        if (next_node !== null) {
          next_node.prev = prev_node;
        }
        if (next_node === null) {
          this.tail = prev_node;
        }
        this.size -= 1;
        return;
      }
      curr = curr.next;
    }
  }

  display() {
    let curr = this.head;
    const arr = [];
    while (curr) {
      arr.push(curr.value.toString());
      curr = curr.next;
    }
    console.log(arr.join("->"));
  }
}

const dll = new DoublyLinkedList();

dll.insert_at_head(2);
dll.insert_at_head(3);
dll.insert_at_tail(4);

dll.display();

//linked list
//remove the nth node from the end of the list and return its head
//from end of list

//will need to use this.val
//this.next refers to another linked list
//tell linked list to no longer point there
//tell 3 to point to 5 instead of 4
//if next is pointing to null, you've reach the end of the list
//backwards from null
//not removing an element

//setting next equal to n away from null + 1
//shouldnt have to create anything new

//this.next

var removeNthFromEnd = function (head, n) {
  let current = head;
  let count = 0;
  while (current !== null) {
    current = current.next;
    count++;
  }
  count = count;
  while (head !== null) {
    if (count < n) {
      console.log("going here", head);
      return head;
    }
    if ((count = n)) {
      head = head.next;
      console.log("going here2", head);
      return head;
    }

    if (count > n) {
      console.log("going here3", head);
      return head;
    }
    console.log("going here4", head);
    head = head.next;
    return head;
  }
};

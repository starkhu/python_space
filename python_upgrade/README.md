
# compare list, dict, set
- list的实现原理是应用数组完成的，因此，单词查询的时间复杂度是O(n)
- dict的实现原理是先对key生成一个hash, 再对hash生成一个红黑树进行查找， 时间复杂度O(logn)
- set的实现原理是用红黑树查找，时间复杂度O(logn)
- dict比set多一个hash的过程
- 查询效率：set > dict > list




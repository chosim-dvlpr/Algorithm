function solution(phone_book) {
    const hashSet = new Map();
    
    phone_book.forEach((p) => hashSet.set(p, ''));
    
    for (let [key, value] of hashSet) {
        for (let i=0; i < key.length; i++) {
            if (hashSet.has(key.substr(0, i))) return false
        }
    }
    return true
}

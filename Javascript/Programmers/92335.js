function check(num) {
    if (num <= 1) return false;

    for (let i=2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    };
    return true;
}

function solution(n, k) {
    const parsedN = n.toString(k)
    const array = parsedN.split('0')
    let result = 0;
    
    array.forEach((a) => {
        if (check(Number(a))) result++;
    })
    return result
}

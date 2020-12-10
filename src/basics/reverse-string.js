

// Trick: Let the last character be at last and keep adding new characters at start
function reverse(str) {
    let newStr = ""
    for (let i = 0; i < str.length; i++) {
        newStr = str[i] + newStr
    }

    return newStr
}

var isPalindrome = function(s) {
    let left = 0;
    let right = s.length - 1;
    while(left < right){
        while(!s[left].match(/^[a-zA-Z0-9]+$/) && left < right){
            left ++;
        }
        while(!s[right].match(/^[a-zA-Z0-9]+$/) && right > left){
            right --;
        }
        if(s[left].toLowerCase() != s[right].toLowerCase()){
            return false;
        }else{
            left ++;
            right --;
        }
    }
    return true;
};
var isValid = function (s) {
  let stack = [];
  const OPENING_BRACES = "([{";
  const CLOSING_BRACES = ")]}";
  const PAIRS = {
    "{": "}",
    "[": "]",
    "(": ")",
  };

  for (let i = 0; i < s.length; i++) {
    if (OPENING_BRACES.includes(s[i])) {
      stack.push(s[i]);
    } else if (CLOSING_BRACES.includes(s[i])) {
      if (!stack.length) {
        return false;
      }
      if (PAIRS[stack.pop()] !== s[i]) {
        return false;
      }
    }
  }

  return !stack.length;
};

console.log(isValid("()[]{}"));

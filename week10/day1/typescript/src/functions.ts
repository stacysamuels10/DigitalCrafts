// () => {}
//parameters, arguments, body, name, return value

const returnTwelve = (): number => {
  return 12;
};

const returnArrayOfNumbers = (num1: number, num2: number): number[] => {
  return [num1, num2];
};

const parsePassword = (password: string): boolean => {
  if (password) {
    return true;
  }
  return false;
};

const calcIncomeTax = (salary: number, state?: string): number => {
  if (state) {
    const total = salary * 1.3;
    return total * 1.2;
  }
  if (salary > 120_000) {
    return salary * 1.3;
  }
  return salary * 1.25;
};

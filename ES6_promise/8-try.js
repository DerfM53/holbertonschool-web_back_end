export default function divideFunction(numerator, denominator) {
  if (denominator > 0) return (denominator / numerator);
  throw new Error('cannot divide by 0');
}

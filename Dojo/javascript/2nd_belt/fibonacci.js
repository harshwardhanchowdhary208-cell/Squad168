function generateFibonacci(n) {
  if (n <= 0) return [];
  if (n === 1) return [0];

  const series = [0, 1]; // Initialize the first two terms
  
  for (let i = 2; i < n; i++) {
    // Add the sum of the last two elements
    series.push(series[i - 1] + series[i - 2]); 
  }
  
  return series;
}

console.log(generateFibonacci(8)); 
// Output: [0, 1, 1, 2, 3, 5, 8, 13]

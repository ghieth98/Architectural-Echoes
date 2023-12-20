/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.vue'],
  theme: {
    fontFamily: {
      'theme-heading': ['Roboto', 'sans-serif'],
      'theme-content': ['Playfair Display', 'serif']
    },
    extend: {
      colors: {
        'theme-primary': '#5368DF',
        'theme-secondary': '#FA5757',
        'theme-grayish-blue': '#9194A1',
        'theme-dark-blue': 'rgb(37, 43, 70)',
        'theme-dark-blue-tp': 'rgba(37, 43, 70, 0.9)',
        'header': '#5F758E',
        'highlight': '#E07A5F',
        'steel-blue': '#468FAF',
        'background': '#F5F5F5',
        'gold-accent': '#DAA520'
      }
    }
  },
  plugins: [require('@tailwindcss/forms')]
}
let tables = document.getElementsByTagName('table');

console.log(tables)
    // tables.forEach((table) => {

let div_overflow = document.createElement('button');

// div_overflow.style.overflow = 'auto';
// div_overflow.style.height = '30px';

// div_overflow.style.background = '#000';

div_overflow.innerHTML = "adas";

tables[1].insertBefore(div_overflow, tables[1]);
// })
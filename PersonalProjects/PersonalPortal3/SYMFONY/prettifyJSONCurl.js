var filename = process.argv.slice(2);
var fs = require('fs');
var obj;
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) throw err;
  obj = JSON.parse(data);
  const formatted = JSON.stringify(obj);
  console.log(formatted);
  fs.writeFileSync(`pretty_${filename}.json`,formatted);
});
console.log(`OK I read ${filename}`);
var full_path_name = process.argv.slice(2)[0];
const path = require('node:path');
console.log(`input full path:|${full_path_name}|`);
const filename = path.basename(full_path_name);
const dirname = path.dirname(full_path_name);
const extension = path.extname(full_path_name);
const pretty_output_path = `${dirname}/pretty_${filename}`;
var fs = require('fs');
var obj;

fs.readFile(full_path_name, 'utf8', function (err, data) {
  console.log(`file: ${filename} read`);
  if (err) throw err;
  obj = JSON.parse(data);
  const formatted = JSON.stringify(obj, null, 4);
  console.log(formatted);
  fs.writeFileSync(pretty_output_path,formatted);
  console.log(`OK now read ${pretty_output_path}`);
});
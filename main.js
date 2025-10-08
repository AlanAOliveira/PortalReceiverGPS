
function teste() {
  // This code runs within an Excel Add-in context
  Excel.run(async (context) => {
    const sheet = context.workbook.worksheets.getActiveWorksheet();

    // Write a value to a specific cell
    sheet.getRange('A1').values = [['Hello, Excel!']];

    // Write an array of values to a range
    const data = [['Name', 'Age'], ['Alice', 28], ['Bob', 35]];
    sheet.getRange('A3:B5').values = data;

    await context.sync();
    console.log('Data written to Excel.');
  });
}

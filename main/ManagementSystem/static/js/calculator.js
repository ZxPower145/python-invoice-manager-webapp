document.addEventListener('DOMContentLoaded', function () {
  function calculateItemTotal(itemNumber) {
    let id_number
    switch (itemNumber) {
      case 1:
        id_number = 'one'
        break
      case 2:
        id_number = 'two'
        break
      case 3:
        id_number = 'three'
        break
      case 4:
        id_number = 'four'
        break
      case 5:
        id_number = 'five'
        break
      default:
        console.error('Something went wrong' + itemNumber)
        break
    }
    let quantityInput = document.getElementById(`id_item_${id_number}_quantity`);
    let unitPriceInput = document.getElementById(`id_item_${id_number}_unit_price`);
    let totalInput = document.getElementById(`id_item_${id_number}_total_price`);
    if (!quantityInput || !unitPriceInput || !totalInput) {
      console.error(`Inputs for item ${id_number} not found.`);
      return;
    }
    function calculateTotal() {
      let quantity = parseFloat(quantityInput.value) || 0;
      let unitPrice = parseFloat(unitPriceInput.value) || 0;
      let total = quantity * unitPrice;
      totalInput.value = total.toFixed(2);
      updateTotalField()
    }
    if (quantityInput && unitPriceInput) {
      quantityInput.addEventListener('change', calculateTotal);
      unitPriceInput.addEventListener('change', calculateTotal);
    } else {
      console.error(`Inputs for item ${itemNumber} not found.`);
    }
    calculateTotal();
  }
  function updateTotalField() {
    let totalField = document.getElementById('total');
    if (!totalField) {
        console.error('Total field not found.');
        return;
    }

    // Calculate the total based on the values of item totals
    let itemOneTotal = parseFloat(document.getElementById('id_item_one_total_price').value) || 0;
    let itemTwoTotal = parseFloat(document.getElementById('id_item_two_total_price').value) || 0;
    let itemThreeTotal = parseFloat(document.getElementById('id_item_three_total_price').value) || 0;
    let itemFourTotal = parseFloat(document.getElementById('id_item_four_total_price').value) || 0;
    let itemFiveTotal = parseFloat(document.getElementById('id_item_five_total_price').value) || 0;

    // Calculate the overall total
    let overallTotal = itemOneTotal + itemTwoTotal + itemThreeTotal + itemFourTotal + itemFiveTotal;
    console.error(overallTotal)
    totalField.value = overallTotal.toFixed(2);
  }
  for (let i = 1; i <= 5; i++) {
      calculateItemTotal(i);
  }
});

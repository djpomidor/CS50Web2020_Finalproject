document.addEventListener('DOMContentLoaded', function() {
  // let closebtns = document.querySelectorAll(".part-btn-close");
  // for (var i = 0; i < closebtns.length; i++) {
  //   closebtns[i].addEventListener("click", function()  {
  //     // Find what was clicked on
  //     const element = event.target;
  //
  //     this.parentElement.style.animationPlayState = 'running';
  //       this.parentElement.addEventListener('animationend', () => {
  //         this.parentElement.parentElement.remove()
  //     });
  //   });
  // };

const partsInput = document.querySelectorAll('input[id^="id_form-"].form-control');
// console.log('!partsInput', partsInput);
partsInput.forEach((item) => {
  item.addEventListener("change", function() {
    let array = ['BLO', 'COV', 'INS'];
    const element = event.target.id;
    for (var i = 0; i < array.length; i++) {
      x = document.querySelector('#id_form-' + i + '-part_name');
      if (element.includes('id_form-' + i)) {
        x.value = array[i];
      }
      console.log("!!!!!!!!!!!!!!!!!!!", element)
    }
  })
});

// partsInput.addEventListener("onchange", function() {
//   array = ['BLO', 'COV', 'INS'];
//   for (var i = 0; i < array.length; i++) {
//     x = document.querySelector('#id_form-' + i + '-part_name');
//     // x.style.display = 'none';
//     x.value =  array[i]
//   }
// })
// console.log('1111', partsInput);
// console.log('2222',matches);

})

function getOrder(number){
  fetch('/orders/' + number)
  .then(response => response.json())
  .then(order => {
    console.log(order)
  })
}

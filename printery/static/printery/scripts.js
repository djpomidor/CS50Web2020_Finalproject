document.addEventListener('DOMContentLoaded', function() {
  let closebtns = document.querySelectorAll(".part-btn-close");
  for (var i = 0; i < closebtns.length; i++) {
    // closebtns[i].addEventListener("click", function()  {
    //   // Find what was clicked on
    //   // const element = event.target;
    //
    //   // this.parentElement.style.animationPlayState = 'running';
    //   //   this.parentElement.addEventListener('animationend', () => {
    //       this.parentElement.parentElement.remove()
    //   // });
    // });
  };
    array = ['BLO', 'COV', 'INS'];

    for (var i = 0; i < array.length; i++) {
      x = document.querySelector('#id_form-' + i + '-part_name');
      // x.style.display = 'none';
      x.value =  array[i]
    }
})

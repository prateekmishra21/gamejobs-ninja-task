function ready(){
  document.getElementById('id_type').addEventListener('change',BookTypeHandler)

}
function BookTypeHandler(e) {
    var type = e.target.value;
    var ebook = document.getElementById('ebook')
    if(type === 'Ebook'){
        ebook.className = 'col-md-12';
        ebook.innerHTML = `
               <div class="form-group">
                     <label style="float:left"><b>Ebook File</b></label>
                  <input type="file" name="ebook" required accept="application/pdf" class="form-control">

               </div>`
    }
    else{
        ebook.className = '';
        ebook.innerHTML = ''
    }
}

window.onload = ready
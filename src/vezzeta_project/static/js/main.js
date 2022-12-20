window.onload=function(){

    let btn = document.getElementById("burger")
    let ul = document.getElementById('ul')
    console.log(btn)

    btn.onclick = ()=>{
        btn.classList.toggle("active")
        ul.classList.toggle("active")
    }
    
  }
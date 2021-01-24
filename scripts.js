window.onload = (event) => {
  ;(function () {
    Array.from(document.querySelectorAll('.arrow')).forEach((item) => {
      item.addEventListener(
        'click',
        function () {
          let con = this.closest('.warningWrapper')
          console.log(con)
          con.classList.toggle('open')
        },
        false
      )
    })
  })()
}

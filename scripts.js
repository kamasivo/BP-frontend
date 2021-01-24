window.onload = (event) => {
  ;(function () {
    Array.from(document.querySelectorAll('.warningWrapper')).forEach((item) => {
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

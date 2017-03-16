// Refresh the Table every 20 seconds
(function update(){
    $.ajax({    
       url: "/cabsharing/",
          success: function(data) {
          $('#the_table').html(data);
          }
          setTimeout(update,30000)
    });
})();
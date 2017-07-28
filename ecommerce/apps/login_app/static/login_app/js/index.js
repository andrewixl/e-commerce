$(document).ready(function(){
  // $('#authcode').hide();
  $('.merchantradio').click(function(){
      if ( $("#authcode").length ){
      }
      else{
        $(".authcode").append('<input type="password" id = "authcode" name="merchant_code" placeholder="Please Enter Merchant Auth Code." size=30><br>');
      }
  })
  $('.consumerradio').click(function(){
    if ( $("#authcode").length ){
      $(".authcode").empty();
    }
  })
});

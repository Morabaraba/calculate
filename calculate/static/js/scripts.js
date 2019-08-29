/* global jQuery _ Backbone */
(function(root, $, _, Backbone) {
    $(main) // on document ready call main

    var calculator = {
        display: '0',
        number1: undefined,
        number2: undefined, 
        waitingForNumber2: false,
        operation: undefined,
        
        $display: undefined
    }
    
    function refreshDisplay() {
        calculator.$display.val(calculator.display)           
    }
    
    function main() {
        calculator.$display = $('.calculator-screen')
        refreshDisplay()
    }

})(window, jQuery, _, Backbone)
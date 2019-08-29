/* global jQuery _ Backbone */
(function(root, $, _, Backbone) {
    $(main) // on document ready call main

    var calculator = {
        display: '0',
        number1: undefined,
        number2: undefined,
        waitingForNumber2: false,
        operation: undefined,

        $display: undefined,
        $keys: undefined
    }

    function refreshDisplay() {
        calculator.$display.val(calculator.display)
    }

    function inputDecimal(dot) {
        if (calculator.waitingForNumber2 === true) return

        if (!_.include(calculator.display, dot)) {
            calculator.display += dot
        }
    }

    function setupKeys() {
        calculator.$keys.on('click', function(event) {
            var $target = $(event.target)

            if ($target.hasClass('operator')) {
                setOperation($target.val())
                refreshDisplay()
                return
            }

            if ($target.hasClass('decimal')) {
                inputDecimal($target.val())
                refreshDisplay()
                return
            }

            if ($target.hasClass('all-clear')) {
                resetCalculator()
                refreshDisplay()
                return
            }

            inputNumber($target.val())
            refreshDisplay()
        })
    }

    function setOperation(val) {
        
        switch (val) {
            case '+':
                calculator.operation = 'addition'
                break
            case '-':
                calculator.operation = 'subtraction'
                break
            case '*':
                calculator.operation = 'multiplication'
                break
            case '/':
                calculator.operation = 'division'
                break
            case '%':
                calculator.operation = 'modulo'
                break
            case 'sqrt':
                calculator.operation = 'sqrt'
                break
            case '=':
                // code block
                break
            default:
                // code block
        }
        
        if (calculator.waitingForNumber2) {
            calculator.number2 = calculator.display
            ajaxOperation()    
            calculator.waitingForNumber2 = false
        } else {
            calculator.number1 = calculator.display
            calculator.waitingForNumber2 = true
        }
            
    }

    function resetCalculator() {
        calculator.display = '0'
        calculator.number1 = undefined
        calculator.number2 = undefined
        calculator.waitingForNumber2 = false
        calculator.operation = undefined
    }

    function inputNumber(number) {

        if (calculator.waitingForNumber2 === true) {
            calculator.display = number
            //calculator.waitingForNumber2 = false
        }
        else {
            calculator.display = calculator.display === '0' ? number : calculator.display + number
        }
    }

    function ajaxOperation() {
        var model = new Backbone.Model({
            number1: calculator.number1, 
            number2: calculator.number2
        })
        model.url = '/ajax/' + calculator.operation
        
        model.on('sync', function (model, response, options) {
            debugger    
        })
        model.on('error', function (model, response, options) {
            debugger    
        })     
        debugger
        model.sync()
    }
    function main() {
        calculator.$display = $('.calculator-screen')
        refreshDisplay()

        calculator.$keys = $('.calculator-keys')
        setupKeys()
    }

})(window, jQuery, _, Backbone)
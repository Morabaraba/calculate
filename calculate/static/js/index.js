/* global jQuery _ Backbone Calculator */
(function(root, $, _, Backbone) {
    $(main) // on document ready call main

    var calculator = {
        machine: new Calculator(),
        display: '0',
        resetDisplayOnInput: false,
        waitingForNumber2: false,
        
        $display: undefined,
        $keys: undefined
    }

    function refreshDisplay() {
        calculator.$display.val(calculator.display)
    }

    function inputDecimal(dot) {
        if (!_.include(calculator.display, dot)) {
            calculator.display += dot
            refreshDisplay()
        }
    }

    function setupKeys() {
        calculator.$keys.on('click', function(event) {
            var $target = $(event.target)

            if ($target.hasClass('operator')) {
                setOperation($target.val())
                return
            }

            if ($target.hasClass('decimal')) {
                inputDecimal($target.val())
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
        calculator.waitingForNumber2 = calculator.machine.waitingForNumber2
        calculator.machine.inputNumber(calculator.display)
        calculator.machine.setOperation(val)
        if (!calculator.machine.checkState()) { // we will not receive a answer from server so reset display
            calculator.display = '0'
            refreshDisplay()
        }

    }

    function resetCalculator(display) {
        calculator.display = '0'
        refreshDisplay()
        calculator.machine.reset()

    }

    function inputNumber(number) {
        if (calculator.resetDisplayOnInput) {
            calculator.resetDisplayOnInput = false
            calculator.display = '0'
        }
        calculator.display = calculator.display === '0' ? number : calculator.display + number
    }

    function main() {
        calculator.$display = $('.calculator-screen')
        refreshDisplay()

        calculator.$keys = $('.calculator-keys').find('button')
        setupKeys()

        calculator.machine.on('answer', function(calc, nr1, nr2) {
            calculator.display = calc.number1
            refreshDisplay()
            if (calc.operation === 'equal' || calculator.waitingForNumber2) {
                calculator.resetDisplayOnInput = true
            }
        })
        
        calculator.machine.on('error', function(calc, nr1, nr2, error, resp) {
            console.error(resp)
            alert(error)
        })
    }

})(window, jQuery, _, Backbone)
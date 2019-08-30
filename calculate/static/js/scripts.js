/* global jQuery _ Backbone */
(function(root, $, _, Backbone) {
    $(main) // on document ready call main

    var calculator = {
        display: '0',
        number1: undefined,
        number2: undefined,
        waitingForNumber2: false,
        operation: undefined,
        chainOpreration: false,

        $display: undefined,
        $keys: undefined
    }

    function refreshDisplay(display) {
        calculator.$display.val(display || calculator.display)
    }

    function inputDecimal(dot) {
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
        calculator.chainOpreration = true
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
                if (calculator.operation) {
                    calculator.chainOpreration = false
                } else if (calculator.waitingForNumber2) {
                    // pass
                }
                else {
                    resetCalculator(calculator.display)
                    return
                }
                break
            default:
                console.error('no operation selected')
                alert('no operation selected')
                return
        }

        if (calculator.waitingForNumber2) {
            calculator.number2 = calculator.display
            if (calculator.operation)
                ajaxOperation()
        }
        else {
            calculator.number1 = calculator.display
            calculator.waitingForNumber2 = true
            calculator.display = '0'
        }

    }

    function resetCalculator(display) {
        refreshDisplay(display)
        calculator.display = '0'
        calculator.number1 = undefined
        calculator.number2 = undefined
        calculator.waitingForNumber2 = false
        calculator.operation = undefined
        calculator.chainOpreration = false
        
    }

    function inputNumber(number) {
        if (calculator.waitingForNumber2 === true) {
            if (calculator.chainOpreration === true) {
                calculator.chainOpreration = false
                calculator.display = '0'
            }
            calculator.display = calculator.display === '0' ? number : calculator.display + number
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
        model.url = 'ajax/' + calculator.operation

        model.on('sync', function(model, response, options) {
            if (response.answer) {
                if (calculator.chainOpreration)
                    nextOprerationNumber(response.answer)
                else
                    resetCalculator(response.answer)
            }
            else {
                console.error(response)
                alert('No answer returned from server, sorry.')
            }
        })

        model.on('error', function(model, response, options) {
            console.error(response)
            alert('Error returned from server, sorry.')
        })

        model.save()
    }

    function nextOprerationNumber(number1) {
        calculator.number1 = number1
        calculator.number2 = undefined
        
        calculator.operation = undefined
        
        calculator.chainOpreration = true
        calculator.display = number1
        refreshDisplay()
    }

    function main() {
        calculator.$display = $('.calculator-screen')
        refreshDisplay()

        calculator.$keys = $('.calculator-keys').find('button')
        setupKeys()
    }

})(window, jQuery, _, Backbone)
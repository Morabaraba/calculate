/* global QUnit Calculator */

QUnit.test("Test addition ( 1 + 1 =)", function(assert) {
   
    var done = assert.async()
    var calculator = new Calculator()
    
    calculator.on('answer', function(calc, nr1, nr2) {

        assert.equal(calc, calculator)
        assert.equal(nr1, '1')
        assert.equal(nr2, '1')
        assert.equal(calc.number1, '2')
        done()
    })
    calculator.on('error', function(calc, nr1, nr2, error) {
        assert.ok(false, 'server error')
        done()
    })

    calculator.inputNumber('1')
    calculator.setOperation('+')
    calculator.checkState()
    calculator.inputNumber('1')
    calculator.setOperation('=')
    calculator.checkState()
})

QUnit.test("Test addition ( 1 + 1 + 1 =)", function(assert) {

    var done = assert.async()
    var done2 = assert.async()
    
    var calculator = new Calculator()
    calculator.on('answer', function(calc, nr1, nr2) {

        assert.equal(calc, calculator)
        if (calc.operation === 'addition') {
            assert.equal(nr1, '1')
            assert.equal(nr2, '1')
            assert.equal(calc.number1, '2')
            done()
            
            calculator.inputNumber('1')
            calculator.setOperation('=')
            calculator.checkState()
        }
        if (calc.operation === 'equal') {
            assert.equal(nr1, '2')
            assert.equal(nr2, '1')
            assert.equal(calc.number1, '3')
            done2()
        }
    })
    calculator.on('error', function(calc, nr1, nr2, error) {
        assert.ok(false, 'server error')
        done()
        done2()
    })

    calculator.inputNumber('1')
    calculator.setOperation('+')
    calculator.checkState()
    
    calculator.inputNumber('1')
    calculator.setOperation('+')
    calculator.checkState()

})

QUnit.test("Test multiplication ( 2 * 2 =)", function(assert) {
    
    var done = assert.async()
    var calculator = new Calculator()
    
    calculator.on('answer', function(calc, nr1, nr2) {

        assert.equal(calc, calculator)
        assert.equal(nr1, '2')
        assert.equal(nr2, '2')
        assert.equal(calc.number1, '4')
        done()
    })
    calculator.on('error', function(calc, nr1, nr2, error) {
        assert.ok(false, 'server error')
        done()
    })

    calculator.inputNumber('2')
    calculator.setOperation('*')
    calculator.checkState()
    calculator.inputNumber('2')
    calculator.setOperation('=')
    calculator.checkState()
})

QUnit.test("Test addition and multiplication ( 1 + 1 + 1 * 2 =)", function(assert) {

    var done = assert.async()
    var done2 = assert.async()
    var done3 = assert.async()
    var done4 = assert.async()
    
    var calculator = new Calculator()
    calculator.on('answer', function(calc, nr1, nr2) {

        assert.equal(calc, calculator)
        if (calc.operation === 'addition') {
            if (calc.number1 === '2') {
                assert.equal(nr1, '1')
                assert.equal(nr2, '1')
                assert.equal(calc.number1, '2')
                done()
                
                calculator.inputNumber('1')
                calculator.setOperation('+')
                calculator.checkState()
                
            } else {
                done2()
                
                calculator.inputNumber('2')
                calculator.setOperation('*')
                calculator.checkState()
            }
        } else
        if (calc.operation === 'multiplication') {
            assert.equal(nr1, '3')
            assert.equal(nr2, '2')
            assert.equal(calc.number1, '6')
            done3()
            
            calculator.setOperation('=')
            calculator.checkState()
        } else
        if (calc.operation === 'equal') {
            assert.equal(nr1, '6')
            assert.equal(nr2, undefined)
            assert.equal(calc.number1, '6')
            done4()
        }
    })
    
    calculator.on('error', function(calc, nr1, nr2, error) {
        assert.ok(false, 'server error')
        done()
        done2()
        done3()
        done4()
    })

    calculator.inputNumber('1')
    calculator.setOperation('+')
    calculator.checkState()

    calculator.inputNumber('1')
    calculator.setOperation('+')
    calculator.checkState()
})

QUnit.test("Test addition and multiplication then equal then addition again ( 1 + 1 + 1 * 2 =, 3 + 3)", function(assert) {

    var done = assert.async()
    var done2 = assert.async()
    var done3 = assert.async()
    var done4 = assert.async()
    var done5 = assert.async()
    
    var calculator = new Calculator()
    calculator.on('answer', function(calc, nr1, nr2) {

        assert.equal(calc, calculator)
        if (calc.operation === 'addition') {
            if (calc.number1 === '2') {
                assert.equal(nr1, '1')
                assert.equal(nr2, '1')
                assert.equal(calc.number1, '2')
                done()
                
                calculator.inputNumber('1')
                calculator.setOperation('+')
                calculator.checkState()
                
            } else 
            if (calc.number1 === '6') {
                done5()
            } else
            {
                done2()
                
                calculator.inputNumber('2')
                calculator.setOperation('*')
                calculator.checkState()
            }
        } else
        if (calc.operation === 'multiplication') {
            assert.equal(nr1, '3')
            assert.equal(nr2, '2')
            assert.equal(calc.number1, '6')
            done3()
            
            calculator.setOperation('=')
            calculator.checkState()
        } else
        if (calc.operation === 'equal') {
            assert.equal(nr1, '6')
            assert.equal(nr2, undefined)
            assert.equal(calc.number1, '6')
            done4()
            
            calculator.inputNumber('3')
            calculator.setOperation('+')
            calculator.checkState()
            
            calculator.inputNumber('3')
            calculator.setOperation('+')
            calculator.checkState()
        }
    })
    
    calculator.on('error', function(calc, nr1, nr2, error) {
        assert.ok(false, 'server error')
        done()
        done2()
        done3()
        done4()
        done5()
    })

    calculator.inputNumber('1')
    calculator.setOperation('+')
    calculator.checkState()

    calculator.inputNumber('1')
    calculator.setOperation('+')
    calculator.checkState()
})

QUnit.test("Test subtraction ( 5 - 4 =)", function(assert) {
   
    var done = assert.async()
    var calculator = new Calculator()
    
    calculator.on('answer', function(calc, nr1, nr2) {

        assert.equal(calc, calculator)
        assert.equal(nr1, '5')
        assert.equal(nr2, '4')
        assert.equal(calc.number1, '1')
        done()
    })
    calculator.on('error', function(calc, nr1, nr2, error) {
        assert.ok(false, 'server error')
        done()
    })

    calculator.inputNumber('5')
    calculator.setOperation('-')
    calculator.checkState()
    calculator.inputNumber('4')
    calculator.setOperation('=')
    calculator.checkState()
})

QUnit.test("Test division ( 5 / 4 =)", function(assert) {
   
    var done = assert.async()
    var calculator = new Calculator()
    
    calculator.on('answer', function(calc, nr1, nr2) {

        assert.equal(calc, calculator)
        assert.equal(nr1, '5')
        assert.equal(nr2, '4')
        assert.equal(calc.number1, '1.25')
        done()
    })
    calculator.on('error', function(calc, nr1, nr2, error) {
        assert.ok(false, 'server error')
        done()
    })

    calculator.inputNumber('5')
    calculator.setOperation('/')
    calculator.checkState()
    calculator.inputNumber('4')
    calculator.setOperation('=')
    calculator.checkState()
})


QUnit.test("Test modulo ( 5 % 4 =)", function(assert) {
   
    var done = assert.async()
    var calculator = new Calculator()
    
    calculator.on('answer', function(calc, nr1, nr2) {

        assert.equal(calc, calculator)
        assert.equal(nr1, '5')
        assert.equal(nr2, '4')
        assert.equal(calc.number1, '1')
        done()
    })
    calculator.on('error', function(calc, nr1, nr2, error) {
        assert.ok(false, 'server error')
        done()
    })

    calculator.inputNumber('5')
    calculator.setOperation('%')
    calculator.checkState()
    calculator.inputNumber('4')
    calculator.setOperation('=')
    calculator.checkState()
})
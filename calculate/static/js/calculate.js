/* global jQuery _ Backbone */

var Calculator = function() {
    var self = this
    _.extend(self, Backbone.Events);
    self.reset()
}

Calculator.prototype.setOperation = function(val) {
    var self = this
    self.operationPrev = self.operation
    switch (val) {
        case '+':
            self.operation = 'addition'
            break
        case '-':
            self.operation = 'subtraction'
            break
        case '*':
            self.operation = 'multiplication'
            break
        case '/':
            self.operation = 'division'
            break
        case '%':
            self.operation = 'modulo'
            break
        case 'sqrt':
            self.operation = 'sqrt'
            break
        case '=':
            self.operation = 'equal'
            break
        default:
            throw new Error('No default operation selected')
    }
}

Calculator.prototype.inputNumber = function(number) {
    var self = this
    if (self.waitingForNumber2) {
        self.number2 = number
    } else {
        self.number1 = number
    }
}

Calculator.prototype.performOperation = function(number1, number2) {
    var self = this
    if (!self.operation) {
        throw new Error('No operation selected')
    }

    if (!self.number1) {
        throw new Error('No number given')
    }

    if (self.operation == 'equal') {
        self.trigger('error', self, number1, number2, 'Select operation')
        throw new Error('No equal operation')
    }
    
    var model = new Backbone.Model({
        number1: number1,
        number2: number2
    })
    model.url = 'ajax/' + self.operation

    model.on('sync', function(model, response, options) {
        if (response.answer) {
            self.number1 = response.answer
            self.number2 = undefined
            self.operationPrev = undefined
            if (self.operationReset) {
                self.operation = self.operationReset
                self.operationReset = undefined
            }
            self.trigger('answer', self, number1, number2)
        }
        else {
            throw new Error('No number given')
        }
    })

    model.on('error', function(model, response, options) {
        //console.error(response)
        self.trigger('error', self, number1, number2, 'server error', response)
        throw new Error('server error')
    })

    model.save()
}

Calculator.prototype.checkState = function() {
    var self = this
    
    if (!self.waitingForNumber2) {
        self.waitingForNumber2 = true
        return false
    }

    switch (self.operation) {
        case 'addition':
            self.performOperation(self.number1, self.number2)
            break
        case 'multiplication':
            self.performOperation(self.number1, self.number2)
            break
        case 'subtraction':
            self.performOperation(self.number1, self.number2)
            break
        case 'division':
            self.performOperation(self.number1, self.number2)
            break
        case 'modulo':
            self.performOperation(self.number1, self.number2)
            break
        case 'sqrt':
            self.performOperation(self.number1, self.number2)
            break
        case 'equal':
            if (!self.number2) {
                self.waitingForNumber2 = false
                self.operationPrev = undefined
                self.trigger('answer', self, self.number1, self.number2)
                return true
            }
            self.operationReset = 'equal'
            self.operation = self.operationPrev
            
            self.performOperation(self.number1, self.number2)
            break
        default:
            throw new Error('No state operation selected')
    }
    return true
}

Calculator.prototype.reset = function() {
    var self = this
    self.number1 = undefined
    self.number2 = undefined
    self.waitingForNumber2 = false
    self.operation = undefined
    self.operationPrev = undefined
    self.operationReset = undefined
}
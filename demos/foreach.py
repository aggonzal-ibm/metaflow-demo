from metaflow import FlowSpec, step


class ForeachFlow(FlowSpec):
    @step
    def start(self):
        self.creatures = ['bird', 'mouse', 'dog']
        self.next(self.analyze_creatures, foreach='creatures')  # A
    
    @step
    def analyze_creatures(self):
        print("Analyzing", self.input)  # B
        self.creature = self.input
        self.score = len(self.creature)
        self.next(self.join)
    
    
    @step
    def join(self, inputs):
        self.best = max(inputs, key=lambda x: x.score).creature
        self.next(self.end)
    
    
    @step
    def end(self):
        print(self.best, 'won!')


if __name__ == '__main__':
    ForeachFlow()
#A A foreach branch is defined with the foreach keyword that refers to a list
#B self.input points to an item of the foreach list 


"""_summary_
        
Este código define una clase llamada ForeachFlow que utiliza el paquete Metaflow para implementar un flujo de trabajo. La clase ForeachFlow hereda de FlowSpec y define cuatro métodos start, analyze_creatures, join y end que representan los diferentes pasos en el flujo de trabajo.

El método start crea una lista de criaturas creatures y utiliza el método next de FlowSpec para especificar que el siguiente paso será llamar al método analyze_creatures para cada elemento en la lista creatures (Línea A).

El método analyze_creatures imprime el input actual (Línea B), asigna el input a la variable creature, calcula una puntuación para cada criatura y utiliza next para ir al siguiente paso join.

El método join utiliza inputs para calcular la criatura con la puntuación más alta y almacenarla en la variable best. Luego, utiliza next para ir al siguiente paso end.

        """

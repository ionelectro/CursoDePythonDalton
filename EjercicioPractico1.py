cursoActual = 1.5
CursoMinimo = 2.5
CursoPromedio = 4
CursoMaximo = 7
DiferenciaDeCursosEnPorcentaje = (CursoMinimo - cursoActual) / CursoMinimo * 100
print("El porcentaje de diferencia entre el curso actual y el mínimo es de: ", DiferenciaDeCursosEnPorcentaje, "%")

DiferenciaDeCursosEnPorcentaje = (CursoPromedio - cursoActual) / CursoPromedio * 100
print("El porcentaje de diferencia entre el curso actual y el promedio es de: ", DiferenciaDeCursosEnPorcentaje, "%")

DiferenciaDeCursosEnPorcentaje = (CursoMaximo - cursoActual) / CursoMaximo * 100
DiferenciaDeCursosEnPorcentaje = round(DiferenciaDeCursosEnPorcentaje, 2)

print("El porcentaje de diferencia entre el curso actual y el máximo es de: ", DiferenciaDeCursosEnPorcentaje, "%")

#CursoActual al ser equivalente a 10 horas a cuanto equivale con respecto al promedio de los demás cursos en horas
CursoActualHoras = cursoActual * 10
CursoPromedioHoras = CursoPromedio * 10
DiferenciaDeCursosEnHoras = CursoPromedioHoras - CursoActualHoras
print("La diferencia entre el curso actual y el promedio en horas es de: ", DiferenciaDeCursosEnHoras, "horas")

#CursoActual al ser equivalente a 10 horas a cuanto equivale con respecto al mínimo de los demás cursos en horas
CursoMinimoHoras = CursoMinimo * 10
DiferenciaDeCursosEnHoras = CursoMinimoHoras - CursoActualHoras
print("La diferencia entre el curso actual y el mínimo en horas es de: ", DiferenciaDeCursosEnHoras, "horas")

#CursoActual al ser equivalente a 10 horas a cuanto equivale con respecto al máximo de los demás cursos en horas
CursoMaximoHoras = CursoMaximo * 10
DiferenciaDeCursosEnHoras = CursoMaximoHoras - CursoActualHoras
print("La diferencia entre el curso actual y el máximo en horas es de: ", DiferenciaDeCursosEnHoras, "horas")




using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _040_Operator_Bit
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 15;
            int b = 22;

            int c = a & b;
            int d = a | b;
            int e = a ^ b;
            Console.WriteLine("a & b: " + c);
            Console.WriteLine("a | b: " + d);
            Console.WriteLine("a ^ b: " + e);

            Console.WriteLine("a << 2: " + (a << 2));
            Console.WriteLine("b >> 2: " + (b >> 2));

            int h = ~b;
            Console.WriteLine("h = ~b: " + h);

            int i = (~b) >> 2;
            Console.WriteLine("i = ~b >> 2: " + i);

        }
    }
}

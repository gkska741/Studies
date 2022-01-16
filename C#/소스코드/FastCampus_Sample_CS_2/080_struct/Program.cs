using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _088_struct
{
    struct AA
    {
        public int x;
        public int y;

        public AA(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
        public void Print()
        {
            Console.WriteLine("x: {0}, y: {1}", x, y);
        }
        static void Main(string[] args) {
            AA aa = new AA(10, 20);
            aa.Print();

        }
    }
}

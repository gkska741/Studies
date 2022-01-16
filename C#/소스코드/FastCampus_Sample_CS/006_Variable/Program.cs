using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*-----------------------------------------------------------------------------
 * Name: _006_Variable
 * DESC: 변수 선언에 기초
-----------------------------------------------------------------------------*/
namespace _006_Variable
{
    class Program
    {
        static void Main(string[] args)
        {
            int num;
            num = 1000;
            Console.WriteLine(num);
            int x = 1000, b = 2000; //선언과 동시에 초기화하는 방법. 위의 코드보다 가독성이 높아졌다.
            Console.WriteLine("x: " + x);
            Console.WriteLine("B: {0}", b);

        }
    }
}

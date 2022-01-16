using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*-----------------------------------------------------------------------------
 * Name: _083_override
 * DESC: 오버라이딩(다형성): 
 * 같은 기능을 하는 함수를 오버라이딩해서 다른 기능을 추가적으로 할 수 있도록...
-----------------------------------------------------------------------------*/
namespace _083_override
{
    class Super
    {
        protected int num = 10;

        public virtual void Print(){
            Console.WriteLine("num:  {0}", num);
        }
    }

    class AA : Super
    {
        public int a = 5;

        public override void Print() {
            base.Print();
            Console.WriteLine("AA a:  {0}", a);
            //Print()함수를 base.Print()를 실행한 후, 내가 실행하는 기능(29번쨰줄)을 추가적으로 실행한다.
        }
    }

    class BB : Super
    {
        public int b = 3;
        public override void Print() {
            base.Print();

            Console.WriteLine("BB b:  {0}", b);
        }
    }

    class Program
    {
        static void Main(string[] args) {
            Super super = new Super();
            super.Print();

            Super aa = new AA();
            aa.Print();

            Super bb = new BB();
            bb.Print();
        }
    }
}

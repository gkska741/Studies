using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/* 0~99까지 랜덤 수를 생성하는 예제 */
/* 이후 2개의 정수 합을 맞추는 프로그램을 작성 */
/* 2개의 정수가 주어진다 -> 다음 두 수의 합을 물어봄 -> 정답이면 정답 출력, 오답이면 정답을 출력해줌) */
namespace _055_Check
{
    class Program
    {
        static void Main(string[] args)
        {
            int prob_num = 1;
            int right_num = 0;
            while (true)
            {
                if (prob_num == 6)
                {
                    break;
                }
                Random rnd = new Random();
                int a = rnd.Next(0, 100);
                int b = rnd.Next(0, 100);
                int answer = a + b;
                Console.WriteLine("{0}: 다음 두 수의 합은 몇?(총5문제)",prob_num);
                Console.WriteLine("{0} + {1} = ??", a, b);

                int my_answer = int.Parse(Console.ReadLine());

                if (my_answer == answer)
                {
                    Console.WriteLine("== 정답 == ");
                    right_num += 1;
                }
                else
                {
                    Console.WriteLine("오답(정답은: {0})", answer);
                }
                prob_num += 1;
            }
            Console.WriteLine("당신은 {0}문제 중 {1}문제를 맞췄습니다.", prob_num - 1, right_num);
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/* 5명의 성적 정수를 입력받아서 최대/최소값 출력 */
namespace _057_Check
{
    class Program
    {
        static void Main(string[] args)
        {
            int max_num = 0;
            int min_num = 100;

            for (int a = 0; a < 5; a ++)
            {
                Console.Write("학생의 성적을 입력하세요: ");
                int score = int.Parse(Console.ReadLine());

                if (score >= max_num)
                {
                    max_num = score;
                }

                if (score <= min_num)
                {
                    min_num = score;
                }

            }
            Console.WriteLine("최대값: {0}, 최소값: {1}", max_num, min_num);
        }
    }
}
